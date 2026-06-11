
def callAPI():
    max_retries = 3
    counter = 0
    success = False
    while not success:
        counter += 1
        if counter == 2:
            print("API call successful!")
            success = True
        elif counter > max_retries:
            print("API call failed after 3 retries.")
            break
        else:
            print(f"API call failed. Retrying... (Attempt {counter})")
def danhgiaModel(promts, results):
    for promt, result in enumerate(zip(promts, results)):
        print(f"promt :  {promt}: ket qua : {result}")
if __name__ == "__main__":
    callAPI()
    promts = ["Tính 1+1", "Dịch chữ Cat", "Viết code web"]
    results = ["2", "Mèo", "Lỗi Error"]
    danhgiaModel(promts, results)