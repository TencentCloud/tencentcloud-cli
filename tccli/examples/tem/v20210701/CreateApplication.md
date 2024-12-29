**Example 1: 创建应用**

创建应用

Input: 

```
tccli tem CreateApplication --cli-unfold-argument  \
    --ApplicationName tem-app \
    --Description 这是一个描述 \
    --CodingLanguage JAVA \
    --RepoType 3
```

Output: 
```
{
    "Response": {
        "Result": "57d58b44-ee28-4db6-acba-c1cb0cxxx",
        "RequestId": "app-xxxxxx"
    }
}
```

