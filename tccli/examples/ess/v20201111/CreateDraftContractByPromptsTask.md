**Example 1: 创建智能合同起草任务**



Input: 

```
tccli ess CreateDraftContractByPromptsTask --cli-unfold-argument  \
    --Operator.UserId yDwayUUckpsz*******rxROEDY8LJBJ9 \
    --Requirement 我公司（深圳市星辰科技有限公司）需要与北京云端数据服务有限公司签订一份软件开发服务合同。

项目概述：
我们需要对方为我们开发一套企业级客户关系管理系统（CRM系统），包括客户信息管理、销售流程管理、数据分析仪表盘等核心模块。

主要需求：
1. 项目总金额为人民币80万元，分三期支付：合同签订后支付30%，中期验收后支付40%，终验收后支付30%。
2. 项目开发周期为6个月，从合同生效之日起计算。
3. 需要乙方提供至少1年的免费维护服务。
4. 源代码和知识产权归甲方所有。
5. 乙方需签署保密协议，对甲方的商业数据和业务逻辑严格保密。
6. 如果项目延期超过30天，甲方有权扣除合同金额的5%作为违约金。
7. 需要明确的验收标准和验收流程。
 \
    --ReferenceTemplateId yD3azUUck****n**UEFfm*Wv6Fm7tFzY \
    --RequirementFileIds yD3aWUUc*********u5ahO3EgYkkoe1E \
    --ContractLanguage zh
```

Output: 
```
{
    "Response": {
        "TaskId": "yD3a5UUc*********E3o0MpRNHSEruSi",
        "RequestId": "cf71b8f1-aa74-491a-abde-5cffc9c9db66"
    }
}
```

