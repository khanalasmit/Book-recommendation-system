from flask import Flask,render_template,request
import pickle
import numpy as np
popular_df=pickle.load(open('C:\\Users\\Acer\\OneDrive\\Documents\\projects\\BookRecommendationSystem\\flaskenc\\popular.pkl','rb'))
pt=pickle.load(open('C:\\Users\\Acer\\OneDrive\\Documents\\projects\\BookRecommendationSystem\\flaskenc\\pt.pkl','rb'))
sim_matrix=pickle.load(open('C:\\Users\\Acer\\OneDrive\\Documents\\projects\\BookRecommendationSystem\\flaskenc\\similarity.pkl','rb'))
Books=pickle.load(open('C:\\Users\\Acer\\OneDrive\\Documents\\projects\\BookRecommendationSystem\\flaskenc\\books.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html'
                           ,book_name=list(popular_df['Book-Title'].values)
                           ,author=list(popular_df['Book-Author'].values)
                           ,image=list(popular_df['Image-URL-M'].values)
                           ,votes=list(popular_df['Num-Ratings'].values)
                           ,rating=list(popular_df['Book-Rating'].values)
                           )

@app.route("/recommend")
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    book_name=request.form.get('user_input')
    #index fetch
    if book_name not in pt.index:
        print(f"'{book_name}' not found in dataset")
        return
    
    index=np.where(pt.index==book_name)[0][0]
    #Get similarities for the correct book (use index, not 0)
    similar_items=sorted(list(enumerate(sim_matrix[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    print(f"Books similar to '{book_name}':")
    data=[]
    for i in similar_items:
        item=[]
        temp_df=Books[Books['Book-Title']==pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        #print(temp_df.drop_duplicates('Book-Title')['Image-URL-M'])
        data.append(item)
    
    print(data)
    return render_template('recommend.html',data=data)
    

if __name__ == "__main__":
    app.run(debug=True)
