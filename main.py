from src.latches import OneBitEdgeTriggeredLatch


def main():
    test_latch = OneBitEdgeTriggeredLatch("test_edge_triggered_latch")
    print("---")
    print("set clock to 1")
    print("---")
    test_latch.clock.val = 1
    print("---")
    print("set data to 1")
    print("---")
    test_latch.data.val = 1
    # FIXME when Q = 0 and data = 1, clock 1->0 results in Q = 1
    print("---")
    print("set clock to 0")
    print("---")
    test_latch.clock.val = 0


if __name__ == "__main__":
    main()
