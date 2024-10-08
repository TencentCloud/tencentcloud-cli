**Example 1: 根据名称匹配边缘函数列表**



Input: 

```
tccli teo DescribeFunctions --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --Filters.0.Name name \
    --Filters.0.Values test \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "FunctionId": "ef-1pakhnuy",
                "ZoneId": "zone-293e7s5jne1i",
                "Content": "addEventListener('fetch', e => {\r\n  const response = new Response('Hello World!');\r\n  e.respondWith(response);\r\n});",
                "Name": "test-function",
                "Remark": "my function",
                "Domain": "test-function-zone-293e7s5jne1i-123456789.eo-edgefunctions1.com",
                "CreateTime": "2022-09-19T15:23:25+08:00",
                "UpdateTime": "2022-09-19T15:27:13+08:00"
            },
            {
                "FunctionId": "ef-2pakw1uk",
                "ZoneId": "zone-293e7s5jne1i",
                "Content": "addEventListener('fetch', e => {\r\n  const response = new Response('Hello World test!');\r\n  e.respondWith(response);\r\n});",
                "Name": "test-function2",
                "Remark": "my function 2",
                "Domain": "test-function-zone-293e7s5jne1i-123456789.eo-edgefunctions1.com",
                "CreateTime": "2022-09-20T15:23:25+08:00",
                "UpdateTime": "2022-09-20T15:27:13+08:00"
            }
        ],
        "TotalCount": 17,
        "RequestId": "ab8a61c5-4eef-45af-9384-b071f1922541"
    }
}
```

**Example 2: 根据函数 ID 匹配边缘函数列表**



Input: 

```
tccli teo DescribeFunctions --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --FunctionIds ef-1pakhnuy \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "FunctionId": "ef-1pakhnuy",
                "ZoneId": "zone-293e7s5jne1i",
                "Content": "addEventListener('fetch', e => {\r\n  const response = new Response('Hello World!');\r\n  e.respondWith(response);\r\n});",
                "Name": "test-function",
                "Remark": "my function",
                "Domain": "test-function-zone-293e7s5jne1i-123456789.eo-edgefunctions1.com",
                "CreateTime": "2022-09-19T15:23:25+08:00",
                "UpdateTime": "2022-09-19T15:27:13+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ab8a61c5-4eef-45af-9384-b071f1922541"
    }
}
```

