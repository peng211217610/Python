from locust import HttpUser,TaskSet,task


class Demo(TaskSet):

    @task(1)
    def baidu(self):
        url = '/huahuage/p/12917114.html'
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        req = self.client.get(url,headers=header,verify=False)

        if req.status_code == 200:
            print("success")
        else:
            print("fails")


class websitUser(HttpUser):
    tasks = [Demo]
    min_wait = 30
    max_wait = 60


if __name__ == "__main__":
    import os

    os.system("locust -f ./locustfile.py --host=https://www.cnblogs.com")