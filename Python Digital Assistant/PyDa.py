import wolframalpha
import wikipedia

while True:
    ques = raw_input("Question: ")
    
    try:
        #wolframalpha
        app_id = "PTXV4K-QRKQLHW54H"
        client = wolframalpha.Client(app_id)
        res = client.query(ques)
        answer = next(res.results).text
        print answer

    except:
        #wikipedia
        print wikipedia.summary(ques).encode('utf-8')