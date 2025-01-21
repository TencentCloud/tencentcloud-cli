**Example 1: 修改应用**

修改应用

Input: 

```
tccli lke ModifyApp --cli-unfold-argument  \
    --AppBizId 1801166480814637056 \
    --AppType knowledge_qa \
    --BaseConfig.Avatar 头像 \
    --BaseConfig.Desc 应用描述 \
    --BaseConfig.Name 我的应用 \
    --AppConfig.KnowledgeQa.Greeting 欢迎语 \
    --AppConfig.KnowledgeQa.Model.Name cs-normal \
    --AppConfig.KnowledgeQa.Model.IsUseContext True \
    --AppConfig.KnowledgeQa.Model.HistoryLimit 1 \
    --AppConfig.KnowledgeQa.Model.AliasName 精调知识大模型标准版 \
    --AppConfig.KnowledgeQa.Model.ContextLimit 0 \
    --AppConfig.KnowledgeQa.Model.Desc  \
    --AppConfig.KnowledgeQa.Model.TokenBalance 0 \
    --AppConfig.KnowledgeQa.Model.Temperature 0.5 \
    --AppConfig.KnowledgeQa.Model.TopP 0.5 \
    --AppConfig.KnowledgeQa.Output.Method 1 \
    --AppConfig.KnowledgeQa.Output.BareAnswer 针对您这个问题，我暂时还无法进行回答，请换一个问题吧。 \
    --AppConfig.KnowledgeQa.Output.UseGeneralKnowledge False \
    --AppConfig.KnowledgeQa.Pattern standard \
    --AppConfig.KnowledgeQa.Plugins.0.PluginId 3ad9ddae-587e-4bcc-ae07-ad13bfb1aaca \
    --AppConfig.KnowledgeQa.Plugins.0.ToolId 0ca8d482-1e77-462b-bc21-xddd7c8f052f69 \
    --AppConfig.KnowledgeQa.RoleDescription 角色：客服
技能：提供客户支持、解决技术问题
说法风格：耐心、友好
性格特点：专业、细心
角色限制：只能回答与产品或服务相关的问题 \
    --AppConfig.KnowledgeQa.Search.0.Confidence 0.2 \
    --AppConfig.KnowledgeQa.Search.0.DocTopN 3 \
    --AppConfig.KnowledgeQa.Search.0.IsEnabled True \
    --AppConfig.KnowledgeQa.Search.0.QaTopN 0 \
    --AppConfig.KnowledgeQa.Search.0.ReplyFlexibility 0 \
    --AppConfig.KnowledgeQa.Search.0.ResourceStatus 0 \
    --AppConfig.KnowledgeQa.Search.0.ShowSearchEngine False \
    --AppConfig.KnowledgeQa.Search.0.Type doc \
    --AppConfig.KnowledgeQa.Search.0.UseSearchEngine False \
    --AppConfig.KnowledgeQa.Search.1.Confidence 0.9 \
    --AppConfig.KnowledgeQa.Search.1.DocTopN 0 \
    --AppConfig.KnowledgeQa.Search.1.IsEnabled True \
    --AppConfig.KnowledgeQa.Search.1.QaTopN 2 \
    --AppConfig.KnowledgeQa.Search.1.ReplyFlexibility 1 \
    --AppConfig.KnowledgeQa.Search.1.ResourceStatus 0 \
    --AppConfig.KnowledgeQa.Search.1.ShowSearchEngine False \
    --AppConfig.KnowledgeQa.Search.1.Type qa \
    --AppConfig.KnowledgeQa.Search.1.UseSearchEngine False \
    --AppConfig.KnowledgeQa.Search.2.Confidence 0 \
    --AppConfig.KnowledgeQa.Search.2.DocTopN 0 \
    --AppConfig.KnowledgeQa.Search.2.IsEnabled False \
    --AppConfig.KnowledgeQa.Search.2.QaTopN 0 \
    --AppConfig.KnowledgeQa.Search.2.ReplyFlexibility 0 \
    --AppConfig.KnowledgeQa.Search.2.ResourceStatus 0 \
    --AppConfig.KnowledgeQa.Search.2.ShowSearchEngine False \
    --AppConfig.KnowledgeQa.Search.2.Type taskflow \
    --AppConfig.KnowledgeQa.Search.2.UseSearchEngine False \
    --AppConfig.KnowledgeQa.Search.3.Confidence 0 \
    --AppConfig.KnowledgeQa.Search.3.DocTopN 0 \
    --AppConfig.KnowledgeQa.Search.3.IsEnabled True \
    --AppConfig.KnowledgeQa.Search.3.QaTopN 0 \
    --AppConfig.KnowledgeQa.Search.3.ReplyFlexibility 0 \
    --AppConfig.KnowledgeQa.Search.3.ResourceStatus 2 \
    --AppConfig.KnowledgeQa.Search.3.ShowSearchEngine False \
    --AppConfig.KnowledgeQa.Search.3.Type search \
    --AppConfig.KnowledgeQa.Search.3.UseSearchEngine True \
    --AppConfig.KnowledgeQa.SearchRange.ApiVarAttrInfos.0.ApiVarId 7a6d67e0-eff1-406b-b092-3b8072c19570 \
    --AppConfig.KnowledgeQa.SearchRange.ApiVarAttrInfos.0.AttrBizId 18537d934840613760 \
    --AppConfig.KnowledgeQa.SearchRange.Condition and \
    --AppConfig.KnowledgeQa.SearchStrategy.StrategyType 0 \
    --AppConfig.KnowledgeQa.SearchStrategy.TableEnhancement False \
    --AppConfig.KnowledgeQa.Workflow.IsEnabled True \
    --AppConfig.KnowledgeQa.Workflow.UsePdl False \
    --AppConfig.KnowledgeQa.SingleWorkflow.WorkflowId 单工作流ID \
    --AppConfig.KnowledgeQa.ThoughtModel.AliasName 精调Function-call模型 \
    --AppConfig.KnowledgeQa.ThoughtModel.ContextLimit 0 \
    --AppConfig.KnowledgeQa.ThoughtModel.Desc  \
    --AppConfig.KnowledgeQa.ThoughtModel.HistoryLimit 0 \
    --AppConfig.KnowledgeQa.ThoughtModel.IsUseContext False \
    --AppConfig.KnowledgeQa.ThoughtModel.Name function-call-pro \
    --AppConfig.KnowledgeQa.ThoughtModel.TokenBalance 0 \
    --AppConfig.KnowledgeQa.ThoughtModel.Temperature 0.5 \
    --AppConfig.KnowledgeQa.ThoughtModel.TopP 0.5
```

Output: 
```
{
    "Response": {
        "AppBizId": "198848848484848",
        "RequestId": "dwec-adsdsdsd-sfsfdsfsf"
    }
}
```

