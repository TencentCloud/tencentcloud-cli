**Example 1: 添加成功**



Input: 

```
tccli waf AddAntiFakeUrl --cli-unfold-argument  \
    --Domain www.test.com \
    --Name rulename \
    --Uri http://www.test.com/a1.html
```

Output: 
```
{
    "Response": {
        "RequestId": "ce58ce20-e508-4c68-9a55-18233f703e6f",
        "Result": "success"
    }
}
```

**Example 2: 添加防篡改url**



Input: 

```
tccli waf AddAntiFakeUrl --cli-unfold-argument  \
    --Domain www.test.com \
    --Name rulename \
    --Uri http://zanyang.qcloudwaf.com/index.html
```

Output: 
```
{
    "Response": {
        "RequestId": "09f0ad6a-cca6-4652-9be0-723d474c2d84",
        "Result": "failure"
    }
}
```

