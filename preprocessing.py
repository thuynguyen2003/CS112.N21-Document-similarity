from underthesea import text_normalize
import re
def chuan_hoa_unicode_dau_cau(text):
  return text_normalize(text)

def viet_thuong(text):
	return text.lower()

# đường dẫn tới file stopwords.txt
path = "sources/stopword.txt"
with open(path, mode = 'r',encoding="utf-8-sig") as f:
  stopwords = f.read().split('\n')
  
def xoa_stopword(text):
  words = []
  for word in text.strip().split():
      if word not in stopwords:
          words.append(word)
  return ' '.join(words)

def chuan_hoa_cau(text):
	text = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',text)
	text = re.sub(r'\s+', ' ', text).strip()
	return text

def tien_xu_ly(doc):
  doc = chuan_hoa_unicode_dau_cau(doc)
  doc = viet_thuong(doc)
  doc = xoa_stopword(doc)
  doc = chuan_hoa_cau(doc)
  return doc