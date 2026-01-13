import requests
import os


def fetch_live_streams():
    # 这里假设直播源在某个公开网页上，以文本形式每行一个链接
    url = 'http://example.com/live_streams.txt'  # 请替换为实际的直播源网址
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"获取直播源时出错: {e}")
        return []


def save_streams_to_file(streams):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/live_streams.txt', 'w', encoding='utf - 8') as file:
        for stream in streams:
            file.write(stream + '\n')


if __name__ == '__main__':
    streams = fetch_live_streams()
    save_streams_to_file(streams)
