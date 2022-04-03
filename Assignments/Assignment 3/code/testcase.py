def test_completely_random(self):
        """ Large Completely Random Test """
        for _ in range(50):
            SIZE = 10005
            NUM_ITEMS_MYSELF = SIZE # has to be <= SIZE
            NUM_ITEMS_OTHER = SIZE # has to be <= SIZE
            
            rand_num_myself_items = random.randint(0, NUM_ITEMS_MYSELF)
            rand_num_other_items = random.randint(0, NUM_ITEMS_OTHER)
            myself_items = random.sample(range(0, SIZE), rand_num_myself_items)
            other_items = random.sample(range(-SIZE, 0), rand_num_other_items)
            myself, other = produce_avl_trees(myself_items, other_items)

            rand_num_corrupted = random.randint(0, rand_num_other_items)
            
            corrupted = []
            indexes = random.sample(range(0, rand_num_other_items), rand_num_corrupted)
            for index in indexes:
                corrupted.append(other_items[index])

            for key in corrupted:
                other_items.remove(key)
            expected = sorted(myself_items + other_items)
            myself.uncorrupted_merge(other, corrupted)
            actual = myself.inorder_traverse()

            # self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
            self.assertEqual(expected, actual, 
                msg="Keys in self are not correct or break the AVL Tree invariant for input \
                    corrupted={} (length={}), t1={} (length={}), t2={} (length={})"
                    .format(corrupted, len(corrupted), myself_items, len(myself_items), other_items, len(other_items)))
            try:
                self.assertTrue(myself.check_balanced(), msg="self is not balanced")
            except AssertionError as e:
                print()
                myself.display()
                raise e