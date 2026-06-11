**Example 1: 获取技能下载链接**



Input: 

```
tccli tcr DescribeSkillDownloadInfo --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --SkillName code-reviewer-2-0-0 \
    --SkillVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "PreSignedDownloadURL": "https://tcr-k**r*****251**0398.cos.ap-guangzho*.myqclo*d.c**/docker/re*i*****v2/bl**s/s**256/7e/***ac6b2d***1***9f847**1*3fc2*648da8f1f36*6b2df21*dd*db927*e4ce3/data?x-co***ec***ty*to*en**p*H*n5*Y4lfP*HMG*Q*****OsrnlHnfc25919f2*43e9e******a80b2a5b3245eK*1ffxZgG1*e***r*C******p*QI*******vt0k**64NRvZ0beZt5p*udTxQ8f**l5b3XbfYYPgic2P2ovr4z-W*Al*FZ2-cxH5ylKrGhDAf8QbVSQO_DlfLwFbjIHUgk5AgvmhAsn7pTkS13epo2iSV5DTklqJTz2PojlDQ8LSwF2WJFHVYaZovG9VwpecOyf-eMxw2h9i99wihxAgK6E6LLGk7wJt-qjDLrF47maRaZOOaktq*9zk5XefvRV6VIs_Q8*6dCAABpAlQP***7QH4pSi0cABLX*Fb8bH6gALKJJOa*Ka*******k-rs8*RogQXDIy06pSyo3D8Xk4AX**bWR9**H5MCupdm4P**&q*sig***l*orithm*sha1&q-a*=AKID*8**RGF9**KuIb4*vbgn2cc*B*ItX3**-1XZ96x2*1-YK*kdkzA8*E*h******Pi&q-si*n-ti**=17745059*2%**17*4**9*02&q-k**-time=1774***902*3*177*509502&q-header-list=host&q-u*l-param-list=x-cos-security-token&q-signature=a8f76aa66fafe30bb0e69356c2021957bbc7f210",
        "RequestId": "6d930ded-6a2c-4d98-b79a-22d689be22ff"
    }
}
```

