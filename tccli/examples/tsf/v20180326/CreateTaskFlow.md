**Example 1: 创建工作流**

创建工作流

Input: 

```
tccli tsf CreateTaskFlow --cli-unfold-argument  \
    --FlowName flow-name-test \
    --ProgramIdList program-6a79x94v \
    --TriggerRule.RepeatInterval 1 \
    --TriggerRule.RuleType 1 \
    --TriggerRule.Expression * 2 * * * ? \
    --TimeOut 1 \
    --FlowEdges.0.PositionX 1 \
    --FlowEdges.0.PositionY 2 \
    --FlowEdges.0.NodeType 1 \
    --FlowEdges.0.NodeName task-name \
    --FlowEdges.0.EdgeType 2 \
    --FlowEdges.0.NodeId node-6a79x94v \
    --FlowEdges.0.ChildNodeId subnode-6a79x94v \
    --FlowEdges.0.CoreNode node-6a79x94v \
    --FlowEdges.0.FlowId flow-6a79x94v \
    --FlowEdges.0.TaskLogId tlog-6a79x94v \
    --FlowEdges.0.TaskId task-6a79x94v \
    --FlowEdges.0.GraphId graph-6a79x94v
```

Output: 
```
{
    "Response": {
        "Result": "flow-6a79x94v",
        "RequestId": "wnoxn-12ns92-nsiu29-374hsy"
    }
}
```

