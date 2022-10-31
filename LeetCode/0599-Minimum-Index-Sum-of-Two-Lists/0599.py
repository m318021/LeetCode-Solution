from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map, map2 = {}, {}
        for i in range(len(list1)):
            map[list1[i]] = map.get(i, 0) + i

        for j in range(len(list2)):
            if list2[j] in map:
                map2[list2[j]] = map[list2[j]] + j

        flag = min(map2.values())

        result = []

        for key in map2:
            if map2[key] == flag:
                result.append(key)

        return result


if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines","Hungry Hunter Steakhouse", "Shogun"]
    output = Solution().findRestaurant(list1, list2)
    print(output)

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    output = Solution().findRestaurant(list1, list2)
    print(output)

    list1 = ["happy", "sad", "good"]
    list2 = ["sad", "happy", "good"]
    output = Solution().findRestaurant(list1, list2)
    print(output)