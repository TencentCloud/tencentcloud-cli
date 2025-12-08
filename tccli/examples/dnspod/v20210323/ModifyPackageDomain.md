**Example 1: 成功1**

 成功1

Input: 

```
tccli dnspod ModifyPackageDomain --cli-unfold-argument  \
    --ResourceId 64e4dbbd \
    --Operation change \
    --DomainId 12615187 \
    --NewDomainId 12615183
```

Output: 
```
{
    "Response": {
        "RequestId": "37ef03f4-f151-432e-b2db-f8664a4ee137"
    }
}
```

**Example 2: 成功示例**

 成功示例

Input: 

```
tccli dnspod ModifyPackageDomain --cli-unfold-argument  \
    --ResourceId 6392cb9b \
    --Operation change \
    --DomainId 12600866 \
    --NewDomainId 12611925
```

Output: 
```
{
    "Response": {
        "RequestId": "152ca659-d453-481e-8be3-f0f04d783a24"
    }
}
```

**Example 3: 套餐更换域名**

 套餐更换域名

Input: 

```
tccli dnspod ModifyPackageDomain --cli-unfold-argument  \
    --Operation change \
    --DomainId 203232 \
    --NewDomainId 4975354
```

Output: 
```
{
    "Response": {
        "RequestId": "561cdfcb-37a6-47de-b3c5-2b038e2c2276"
    }
}
```

**Example 4: 套餐绑定域名**

 套餐绑定域名

Input: 

```
tccli dnspod ModifyPackageDomain --cli-unfold-argument  \
    --Operation bind \
    --ResourceId a4d4cec3 \
    --NewDomainId 4975354
```

Output: 
```
{
    "Response": {
        "RequestId": "561cdfcb-37a6-47de-b3c5-2b038e2c2276"
    }
}
```

**Example 5: 套餐解绑域名**

 套餐解绑域名

Input: 

```
tccli dnspod ModifyPackageDomain --cli-unfold-argument  \
    --Operation unbind \
    --ResourceId a4d4cec3
```

Output: 
```
{
    "Response": {
        "RequestId": "561cdfcb-37a6-47de-b3c5-2b038e2c2276"
    }
}
```

