
def xuly_ML(raw):
    new_raw = raw.strip().split()
    print(new_raw)
    final_raw = new_raw[7:10:1]
    print(final_raw)

if __name__ == '__main__':
    raw_output = "   \n\n THOUGHT: I should extract the entities. \nRESULT: apple, banana, cherry   ###   "
    xuly_ML(raw_output)