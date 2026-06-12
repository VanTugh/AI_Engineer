from collections import Counter
def bai1(*args):
    for arg in args:
        batch_size, channels, frames, height, width = arg
        spatial_dims = [i*2 for i in (frames, height, width)]
        return  spatial_dims
def bai2(*args):
    count = Counter(args)
    top1 = count.most_common(1)
    return count, top1
if __name__ == "__main__":
    video_shape = (16, 3, 30, 256, 256)
    sqp = bai1(video_shape)
    print(sqp)
    preds = ["cat", "dog", "cat", "bird", "cat", "dog"]
    count, top1 = bai2(*preds)
    print(count)
    print(top1)