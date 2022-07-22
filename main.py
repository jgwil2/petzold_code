from src.latches import OneBitEdgeTriggeredLatch


def main():
    test_latch = OneBitEdgeTriggeredLatch("test_edge_triggered_latch")
    print("---")
    print("set clock to 1")
    print("---")
    test_latch.clock.setExternalPin(1)
    print("---")
    print("set data to 1")
    print("---")
    test_latch.data.setExternalPin(1)
    print("---")
    print("set clock to 0")
    print("---")
    test_latch.clock.setExternalPin(0)


if __name__ == "__main__":
    main()
