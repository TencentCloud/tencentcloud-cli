**Example 1: 添加规则**



Input: 

```
tccli tcss AddEditAbnormalProcessRule --cli-unfold-argument  \
    --RuleInfo.IsEnable True \
    --RuleInfo.RuleName customrule_20241014050108 \
    --RuleInfo.ImageIds sha256:80d28bedfe5dec59da9ebf8e6260224ac9008ab5c11dbbe16ee3ba3e4439ac2c sha256:8652b9f0cb4c0599575e5a003f5906876e10c1ceb2ab9fe1786712dac14a50cf sha256:5d0da3dc976460b72c77d94c8a1ad043720b0416bfc16c52c45d4847e53fadb6 sha256:84b0f3f7f6f0416a2a8ef19ac765f43887503bd1ba4c81cb6fd2a4eb3da4e867 sha256:c059bfaa849c4d8e4aecaeb3a10c2d9b3d85f5165c66ad3a4d937758128c4d18 sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9 sha256:e57cb8aaa6a5a547a38bff69f54b86f1e9ed86a4ea8246f88ada3b0aa698cde0 sha256:d41059c812a8741c15695046857b90747aef9c7f9d67733962d7bbb025b9d159 sha256:7f8e468621fd9dc3eda2ea2294d684876c68d5df715bb18bd1caa3edabdde4b8 sha256:1ca2c2a1b554474b067257607aa811d191bd3314cb4c31f73eee7d97bed3ff98 \
    --RuleInfo.RuleId 670c35146a91d09858cd8398 \
    --RuleInfo.ChildRules.0.ProcessPath /root/customrule_20241014050108.out \
    --RuleInfo.ChildRules.0.RuleId 670c35146a91d09858cd8399 \
    --RuleInfo.ChildRules.0.RuleLevel HIGH \
    --RuleInfo.ChildRules.0.RuleMode RULE_MODE_ALERT
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

**Example 2: 编辑规则**



Input: 

```
tccli tcss AddEditAbnormalProcessRule --cli-unfold-argument  \
    --RuleInfo.IsEnable True \
    --RuleInfo.RuleName customrule_20241014050108 \
    --RuleInfo.ImageIds sha256:80d28bedfe5dec59da9ebf8e6260224ac9008ab5c11dbbe16ee3ba3e4439ac2c sha256:8652b9f0cb4c0599575e5a003f5906876e10c1ceb2ab9fe1786712dac14a50cf sha256:5d0da3dc976460b72c77d94c8a1ad043720b0416bfc16c52c45d4847e53fadb6 sha256:84b0f3f7f6f0416a2a8ef19ac765f43887503bd1ba4c81cb6fd2a4eb3da4e867 sha256:c059bfaa849c4d8e4aecaeb3a10c2d9b3d85f5165c66ad3a4d937758128c4d18 sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9 sha256:e57cb8aaa6a5a547a38bff69f54b86f1e9ed86a4ea8246f88ada3b0aa698cde0 sha256:d41059c812a8741c15695046857b90747aef9c7f9d67733962d7bbb025b9d159 sha256:7f8e468621fd9dc3eda2ea2294d684876c68d5df715bb18bd1caa3edabdde4b8 sha256:1ca2c2a1b554474b067257607aa811d191bd3314cb4c31f73eee7d97bed3ff98 \
    --RuleInfo.RuleId 670c35146a91d09858cd8398 \
    --RuleInfo.ChildRules.0.ProcessPath /root/customrule_20241014050108.out \
    --RuleInfo.ChildRules.0.RuleId 670c35146a91d09858cd8399 \
    --RuleInfo.ChildRules.0.RuleLevel HIGH \
    --RuleInfo.ChildRules.0.RuleMode RULE_MODE_ALERT
```

Output: 
```
{
    "Response": {
        "RequestId": "055e66ea-9a62-4315-900c-fd7bca22b3a7"
    }
}
```

