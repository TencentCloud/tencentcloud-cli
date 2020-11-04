**Example 1: 获取所有主机标签**

获取所有主机标签

Input: 

```
tccli yunjing DescribeTags --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 2,
                "Name": "标签名",
                "Count": 123
            }
        ],
        "RequestId": "b12a5e5a-9393-453f-a4d9-b42de0b2bcec"
    }
}
```

