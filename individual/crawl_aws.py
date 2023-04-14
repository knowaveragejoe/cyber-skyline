import requests

base_url = "http://metadata.services.cityinthe.cloud:1338"
output_file = "crawl_output.txt"

def is_directory(line):
    return line.endswith("/")

def crawl_directory(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # print(f"Error: {e}")
        return

    content = response.text.strip()
    lines = content.split("\n")

    for line in lines:
        new_url = f"{url.rstrip('/')}/{line.strip('/')}"
        if is_directory(line):
            crawl_directory(new_url + "/", output_file)
        else:
            try:
                response = requests.get(new_url)
                if response.status_code == "404":
                    continue
                with open(output_file, "a") as f:
                    f.write(f"{response.text}\n")
                crawl_directory(new_url, output_file)
            except requests.exceptions.HTTPError as e:
                print(f"Error: {e}")

def main():
    initial_url = f"{base_url}/latest/"
    crawl_directory(initial_url, output_file)

if __name__ == "__main__":
    main()
