def bai1(input_data):
    data = {"role" : "assistant" , "content" : "Hi bro!"}
    input_data.append(data)
    my_message = input_data[1].get("content")
    print(my_message)
    return input_data, my_message

def bai2(input_data1 , input_data2):
    input_data1 = set(input_data1)
    input_data2 = set(input_data2)
    new_data = input_data1.intersection(input_data2)
    print(new_data)

if __name__ == '__main__':
    messages = [
        {"role": "system", "content": "You are a helpful AI."},
        {"role": "user", "content": "Hello!"}
    ]
    print(messages)
    new_message, my_mess = bai1(messages)
    print(new_message)
    print(my_mess)
    doc_1 = ["ai", "is", "the", "future"]
    doc_2 = ["python", "is", "the", "key", "for", "ai"]
    new_data = bai2(doc_1, doc_2)
    print(new_data)
