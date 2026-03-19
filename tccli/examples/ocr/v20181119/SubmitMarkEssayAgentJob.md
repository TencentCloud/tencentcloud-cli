**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli ocr SubmitMarkEssayAgentJob --cli-unfold-argument  \
    --ImageUrlList https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --QuestionConfigMap {"StructureAndContent":"1"}
```

Output: 
```
{
    "Response": {
        "JobIds": [
            "1395596000423952384"
        ],
        "RequestId": "d1a86ab4-1366-4f03-882c-ae3c9f938be6"
    }
}
```

**Example 2: 调用成功示例2**

调用成功示例2

Input: 

```
tccli ocr SubmitMarkEssayAgentJob --cli-unfold-argument  \
    --ImageBase64List data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB*****JoAAAYyCAYAAAB3uYQsAAAQAElEQVR4Aez9aZBkWXodiJ1zn7vHHpFL \
    --QuestionConfigMap {"StructureAndContent":"1"}
```

Output: 
```
{
    "Response": {
        "JobIds": [
            "1395596000423952234"
        ],
        "RequestId": "d1a86ab4-1366-4f03-882c-ae3c9f938be6"
    }
}
```

