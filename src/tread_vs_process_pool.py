import timeit
import requests
import math

from functools import partial
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def download_image(img_url):
    img_bytes = requests.get(img_url).content


_primes = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

img_urls = [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]


def run_with_proccess_pool_primes(values):

    with ProcessPoolExecutor(max_workers=5) as executor:
        result = executor.map(is_prime, values)

    return list(result)


def run_with_thread_pool_primes(values):

    with ThreadPoolExecutor(max_workers=5) as executor:
        result = executor.map(is_prime, values)

    return list(result)


def run_with_proccess_pool_images(images):

    with ProcessPoolExecutor(max_workers=5) as executor:
        result = executor.map(download_image, images)

    return list(result)


def run_with_thread_pool_images(images):

    with ThreadPoolExecutor(max_workers=5) as executor:
        result = executor.map(download_image, images)

    return list(result)


def main():
    pp_time = timeit.timeit(
        partial(run_with_proccess_pool_primes, _primes), number=10)
    tp_time = timeit.timeit(
        partial(run_with_thread_pool_primes, _primes), number=10)
    print(f"Process pool time: {pp_time}")
    print(f"Thread pool time: {tp_time}")

    # pp_time = timeit.timeit(partial(run_with_proccess_pool_images, img_urls), number=10)
    # tp_time = timeit.timeit(partial(run_with_thread_pool_images, img_urls), number=10)
    # print(f"Process pool image download time: {pp_time}")
    # print(f"Thread pool download time: {tp_time}")


if __name__ == "__main__":
    main()
