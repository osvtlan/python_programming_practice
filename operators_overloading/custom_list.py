class CustomList(list):
    def __add__(self, second_list):
        result = CustomList(self)
        for i in range(len(second_list)):
            if i < len(result):
                result[i] += second_list[i]
            else:
                result.append(second_list[i])
        return result

    def __radd__(self, second_list):
        return self.__add__(second_list)

    def __sub__(self, second_list):
        result = CustomList(self)
        for i in range(len(second_list)):
            if i < len(result):
                result[i] -= second_list[i]
            else:
                result.append(-second_list[i])
        return result

    def __rsub__(self, second_list):
        return CustomList([-x for x in self]) + second_list

    def __eq__(self, second_list):
        return sum(self) == sum(second_list)

    def __ne__(self, second_list):
        return sum(self) != sum(second_list)

    def __gt__(self, second_list):
        return sum(self) > sum(second_list)

    def __ge__(self, second_list):
        return sum(self) >= sum(second_list)

    def __lt__(self, second_list):
        return sum(self) < sum(second_list)

    def __le__(self, second_list):
        return sum(self) <= sum(second_list)

    def __str__(self):
        return f"CustomList({super().__str__()}, Sum: {sum(self)})"
