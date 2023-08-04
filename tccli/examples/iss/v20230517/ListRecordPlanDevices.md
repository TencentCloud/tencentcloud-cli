**Example 1: 按照组织名称查询**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --OrganizationName 201 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {}
}
```

**Example 2: 按照设备名称查询**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --DeviceName NVR05 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {}
}
```

**Example 3: 按照通道名称查询**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --ChannelName 11 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {}
}
```

**Example 4: 无查询条件**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {}
}
```

