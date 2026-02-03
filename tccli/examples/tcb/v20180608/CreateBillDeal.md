**Example 1: 变配云开发baas套餐**

指定当前生效套餐和变配目标套餐；指定目标变配资源/环境；（示例将个人版套餐变配为团队版套餐）

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "2a317487-4ca1-4edc-80aa-e2c300f5f7ae"
    }
}
```

**Example 2: 新购云开发baas套餐**

购买云开发baas个人版套餐，购买时长1个月，指定环境别名为cloud，开启超限按量

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d5ce71e0-cf6e-4387-90e4-a4a1ed0f2a8d"
    }
}
```

**Example 3: 新购云开发baas套餐教育体验版**

新购baas教育体验版

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a9487229-4a54-468c-b5f9-900ab9d0387c"
    }
}
```

**Example 4: 新购云开发大促包**

给指定环境加购flexdb大促包，大促包时长1天

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "0ac4bb6a-9a74-4390-bcf1-51b4938d83d0"
    }
}
```

**Example 5: 新购云开发资源包**

给指定环境购买调用次数资源包，购买时长固定为一个月

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d0ff4d25-f803-46f1-80dc-3b36af94af39"
    }
}
```

**Example 6: 续费云开发baas套餐**

给指定套餐/环境续费指定时长，时长单位为月

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "e45941ab-9a88-49df-8626-188a8d6c7236"
    }
}
```

**Example 7: 创建环境并指定资源类型和CAM标签**

购买新环境，并指定所需资源类型，以及自动绑定CAM标签

Input: 

```
tccli tcb CreateBillDeal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "64a8e42d-0372-42b1-b933-8a05715d29bf"
    }
}
```

