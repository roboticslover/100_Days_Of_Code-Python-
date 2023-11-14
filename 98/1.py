# MultiProcessing in Python

import multiprocessing
import requests


def downloadfile(url, name):
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")


def main():
    url = "https://picsum.photos/2000/3000"

    # Create a list to store the processes
    processes = []

    for i in range(3):
        # Create a multiprocessing Process for each download
        p = multiprocessing.Process(target=downloadfile, args=(url, i))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
