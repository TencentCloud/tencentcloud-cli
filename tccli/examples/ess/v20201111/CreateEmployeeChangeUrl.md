**Example 1: 生成员手机号变更链接-不指定手机号**

修改员工手机号

Input: 

```
tccli ess CreateEmployeeChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp9yUuO4zjEwqXwsIljA \
    --UserId yDRt2UUgygqxyp9yUuO4zjEwqXwsIljA
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1741332331,
        "MiniAppPath": "/pages/guide/index?shortKey=yDtSJUde8JFIMAykHz79",
        "RequestId": "s1740727531055190955"
    }
}
```

**Example 2: 生成员手机号变更链接-指定手机号**



Input: 

```
tccli ess CreateEmployeeChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp9yUuO4zjEwqXwsIljA \
    --UserId yDRt2UUgygqxyp9yUuO4zjEwqXwsIljA \
    --NewMobile 13200001111
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1741332331,
        "MiniAppPath": "/pages/guide/index?shortKey=yDtSJUde8JFIMAykHz79",
        "RequestId": "s1740727531055190955"
    }
}
```

