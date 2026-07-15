**Example 1: 创建单台物理机实例**

在广州一区创建一台物理机实例，使用 CentOS 7.9 镜像，并启用 IPv6。

Input: 

```
tccli edgezone CreateInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-1 \
    --InstanceType BMS5.MEDIUM8 \
    --ImageId img-centos-7.9 \
    --InstanceName my-epm-instance \
    --InstanceCount 1 \
    --VersionNumber 7.9.2009 \
    --PrivateNetworkId net-private-001 \
    --PublicNetworkId net-public-001 \
    --EnableIpv6 True
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-abcd1234"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 批量创建物理机实例**

批量创建3台物理机实例。

Input: 

```
tccli edgezone CreateInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-1 \
    --InstanceType BMS5.MEDIUM8 \
    --ImageId img-centos-7.9 \
    --InstanceName batch-instance \
    --InstanceCount 3 \
    --PrivateNetworkId net-private-001 \
    --PublicNetworkId net-public-001
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-abcd1234",
            "ins-efgh5678",
            "ins-ijkl9012"
        ],
        "RequestId": "b5d7b923-6a8c-4e2f-9f01-4e7e8d3c1a2b"
    }
}
```

**Example 3: 批量创建物理机实例（部分成功）**

批量创建3台物理机实例，其中2台创建成功，1台因资源不足创建失败。

Input: 

```
tccli edgezone CreateInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-1 \
    --InstanceType BMS5.MEDIUM8 \
    --ImageId img-centos-7.9 \
    --InstanceName batch-instance \
    --InstanceCount 3 \
    --PrivateNetworkId net-private-001 \
    --PublicNetworkId net-public-001
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-abcd1234",
            "ins-efgh5678"
        ],
        "FailedCount": 1,
        "RequestId": "c7e8f012-3a4b-5c6d-7e8f-9a0b1c2d3e4f"
    }
}
```

