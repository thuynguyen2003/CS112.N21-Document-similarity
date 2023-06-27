import gradio as gr
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import tien_xu_ly


    
def my_cosine_similarity(vec_doc1, vec_doc2):
  vec_doc1 = np.array(vec_doc1).reshape(1, -1)
  vec_doc2 = np.array(vec_doc2).reshape(1, -1)
  cosine = np.sum(vec_doc1*vec_doc2)/ (np.sqrt(np.sum(vec_doc1*vec_doc1)) * np.sqrt(np.sum(vec_doc2*vec_doc2)))
  return cosine

with open("model/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)
    
def text_similarity(text1, text2):
    doc1 = tien_xu_ly(text1)
    doc2 = tien_xu_ly(text2)
    vector = tfidf.transform([doc1, doc2])
    vector1 , vector2= vector[0].toarray()[0], vector[1].toarray()[0]
    return round(my_cosine_similarity(vector1, vector2), 3)

def file_similarity(file1, file2):
    try:
        with open(file1.name, "r", encoding="utf-8-sig") as f:
            text1 = f.read()
        
        with open(file2.name, "r", encoding="utf-8-sig") as f:
            text2 = f.read()
    except:
        return "Lỗi định dạng file"
    doc1 = tien_xu_ly(text1)
    doc2 = tien_xu_ly(text2)
    vector = tfidf.transform([doc1, doc2])
    vector1 , vector2= vector[0].toarray()[0], vector[1].toarray()[0]
    return round(my_cosine_similarity(vector1, vector2), 3)

with gr.Blocks() as CS112:
    gr.Markdown(
        """
        # CS112 - Phân tích và thiết kế thuật toán
        #### Đánh giá độ tương tự giữa hai văn bản
        """
    )
    with gr.Tab("Văn bản"):
        with gr.Row():
            input_text = [gr.Textbox(label="Văn bản 1", lines=5), gr.Textbox(label="Văn bản 2", lines=5)]
        with gr.Row():
            text_button = gr.Button("Đánh giá")
        text_output = gr.Textbox(label="Độ tương tự giữa 2 văn bản là:", lines=2)
    with gr.Tab("File"):
        with gr.Row():
            input_file = [gr.File(file_types=[".txt"], label="Văn bản 1"), gr.File(file_types=[".txt"], label="Văn bản 2")]
        with gr.Row():
            file_button = gr.Button("Đánh giá")
        file_output = gr.Textbox(label="Độ tương tự giữa 2 văn bản là:", lines=2)

    text_button.click(text_similarity, inputs=input_text, outputs=text_output)
    file_button.click(file_similarity, inputs=input_file, outputs=file_output)

CS112.launch()