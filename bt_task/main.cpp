#include <behaviortree_cpp/bt_factory.h>
#include <iostream>

using namespace BT;

/* ------------------- ROOM DOOR ACTIONS ------------------- */

class MoveToRoomDoor : public SyncActionNode
{
public:
    MoveToRoomDoor(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Moving to room door\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

class IsDoorClosed : public ConditionNode
{
public:
    IsDoorClosed(const std::string& name, const NodeConfig& config)
        : ConditionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Checking if door is closed\n";
        return NodeStatus::FAILURE;   // simulate closed door
    }

    static PortsList providedPorts(){ return {}; }
};

class OpenDoor : public SyncActionNode
{
public:
    OpenDoor(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Opening door\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

class EnterRoom : public SyncActionNode
{
public:
    EnterRoom(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Entering room\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

/* ------------------- FRIDGE ACTIONS ------------------- */

class MoveToFridge : public SyncActionNode
{
public:
    MoveToFridge(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Moving to fridge\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

class IsFridgeClosed : public ConditionNode
{
public:
    IsFridgeClosed(const std::string& name, const NodeConfig& config)
        : ConditionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Checking if fridge door is closed\n";
        return NodeStatus::FAILURE;   // simulate closed fridge
    }

    static PortsList providedPorts(){ return {}; }
};

class OpenFridge : public SyncActionNode
{
public:
    OpenFridge(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Opening fridge\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

class FindApple : public SyncActionNode
{
public:
    FindApple(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Finding apple\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

class PickApple : public SyncActionNode
{
public:
    PickApple(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Picking apple\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

class CloseFridge : public SyncActionNode
{
public:
    CloseFridge(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Closing fridge\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

/* ------------------- EXIT ACTION ------------------- */

class ExitRoom : public SyncActionNode
{
public:
    ExitRoom(const std::string& name, const NodeConfig& config)
        : SyncActionNode(name, config) {}

    NodeStatus tick() override
    {
        std::cout << "Exiting room\n";
        return NodeStatus::SUCCESS;
    }

    static PortsList providedPorts(){ return {}; }
};

/* ------------------- MAIN ------------------- */

int main()
{
    BehaviorTreeFactory factory;

    factory.registerNodeType<MoveToRoomDoor>("MoveToRoomDoor");
    factory.registerNodeType<IsDoorClosed>("IsDoorClosed");
    factory.registerNodeType<OpenDoor>("OpenDoor");
    factory.registerNodeType<EnterRoom>("EnterRoom");

    factory.registerNodeType<MoveToFridge>("MoveToFridge");
    factory.registerNodeType<IsFridgeClosed>("IsFridgeClosed");
    factory.registerNodeType<OpenFridge>("OpenFridge");
    factory.registerNodeType<FindApple>("FindApple");
    factory.registerNodeType<PickApple>("PickApple");
    factory.registerNodeType<CloseFridge>("CloseFridge");

    factory.registerNodeType<ExitRoom>("ExitRoom");

    static const char* xml_text = R"(

<root BTCPP_format="4" main_tree_to_execute="MainTree">

  <BehaviorTree ID="MainTree">

    <Sequence>

      <MoveToRoomDoor/>

      <Fallback>
        <IsDoorClosed/>
        <OpenDoor/>
      </Fallback>

      <EnterRoom/>

      <MoveToFridge/>

      <Fallback>
        <IsFridgeClosed/>
        <OpenFridge/>
      </Fallback>

      <FindApple/>
      <PickApple/>
      <CloseFridge/>

      <MoveToRoomDoor/>
      <ExitRoom/>

    </Sequence>

  </BehaviorTree>

</root>

)";

    auto tree = factory.createTreeFromText(xml_text);

    tree.tickWhileRunning();

    return 0;
}