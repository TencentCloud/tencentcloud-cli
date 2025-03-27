**Example 1: SyncExecuteCommandOnAndroidInstances 示例**



Input: 

```
tccli gs SyncExecuteCommandOnAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds cai-1300055477-ea990LbMLbq \
    --Command ls
```

Output: 
```
{
    "Response": {
        "CommandResults": [
            {
                "InstanceId": "cai-1300055477-ea990LbMLbq",
                "Output": "{\"StdOut\":\"acct\\napex\\nbin\\nbugreports\\ncache\\ncharger\\nconfig\\ncontainer.prop\\nd\\ndata\\ndebug_ramdisk\\ndefault.prop\\ndev\\netc\\ninit\\ninit.environ.rc\\ninit.rc\\ninit.usb.rc\\ninit.zygote32.rc\\ninit.zygote64_32.rc\\nlost+found\\nmetadata\\nmnt\\nodm\\noem\\nproc\\nproduct\\nproduct_services\\nres\\nsbin\\nsdcard\\nstorage\\nsys\\nsystem\\ntcg_share_data\\nueventd.rc\\nvendor\\nwebrtc_ctrl_20240914.log\\nwebrtc_ctrl_20240915.log\\nwebrtc_ctrl_20240916.log\\nwebrtc_ctrl_20240917.log\\nwebrtc_ctrl_20240918.log\\nwebrtc_ctrl_20240919.log\\n\",\"StdError\":\"\"}",
                "Status": "SUCCESS"
            }
        ],
        "RequestId": "bc62efee-0e09-4267-9f0b-aabdc80bf2eb"
    }
}
```

