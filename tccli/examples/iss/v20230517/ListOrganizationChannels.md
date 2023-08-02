**Example 1: 按照设备名称查询**

 

Input: 

```
tccli iss ListOrganizationChannels --cli-unfold-argument  \
    --OrganizationId 182 \
    --DeviceName abc \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {}
}
```

**Example 2: 按照通道名称查询**

 

Input: 

```
tccli iss ListOrganizationChannels --cli-unfold-argument  \
    --OrganizationId 182 \
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

**Example 3: 无查询条件**

 

Input: 

```
tccli iss ListOrganizationChannels --cli-unfold-argument  \
    --OrganizationId 182 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {}
}
```

