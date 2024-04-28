**Example 1: 1212**



Input: 

```
tccli rum DescribeRumLogExport --cli-unfold-argument  \
    --Query id:1 \
    --EndTime 1 \
    --Name  \
    --StartTime 1665994920000 \
    --ID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "763188d1-9f99-45e8-8bbf-bcdffa8f58f0",
        "Result": ""
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumLogExport --cli-unfold-argument  \
    --Name logDemo \
    --Fields date \
    --StartTime 1714103013 \
    --Query * \
    --EndTime 1714103013 \
    --ID 0
```

Output: 
```
{
    "Response": {
        "Result": "Traceback (most recent call last):\n  File \"/opt/app-root/lib64/python3.8/site-packages/tornado/web.py\", line 1763, in _execute\n    result = self.prepare()\n  File \"/opt/app-root/lib64/python3.8/site-packages/tornado/web.py\", line 2538, in prepare\n    raise HTTPError(self._status_code)\ntornado.web.HTTPError: HTTP 404: Not Found\n",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

