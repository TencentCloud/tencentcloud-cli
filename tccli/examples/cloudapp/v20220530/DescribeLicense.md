**Example 1: 云应用许可校验接口**

云应用准备更新 LICENCE 校验的接口

Input: 

```
tccli cloudapp DescribeLicense --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Token": "eyJhbGciOi",
        "RequestId": "2aab88d8-b5bd-42ea-92ee-f8df1228e278"
    }
}
```

**Example 2: 云应用许可校验接口 带增购信息**

云应用准备更新 LICENCE 校验的接口带增购信息

Input: 

```
tccli cloudapp DescribeLicense --cli-unfold-argument  \
    --Filters.0.Name QueryType \
    --Filters.0.Values IncludeAddition
```

Output: 
```
{
    "Response": {
        "Token": "eyJhbGciOi",
        "RequestId": "f3891f61-7c21-4223-9b5b-33a3e7ca3095"
    }
}
```

