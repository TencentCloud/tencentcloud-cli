**Example 1: 开启NAT集群防火墙Bypass**

开启NAT集群防火墙的Bypass模式，禁用正常下一跳使流量绕过防火墙

Input: 

```
tccli cfw ModifyClusterFwBypass --cli-unfold-argument  \
    --FwType NAT_FW \
    --CcnId ccn-iidlg5oh \
    --Enable False \
    --NatInsId nat-nlq8cmtw
```

Output: 
```
{
    "Response": {
        "RequestId": "1bf5e5a2-2a1d-4284-bbea-29d504e7a3d7"
    }
}
```

