"""
아래에 학번과 이름을 꼭 적으세요.

학번:60131271
이름:최다한


- 각 문제는 총 25점입니다. 
- 리스트에 저장된 값의 개수를 n이라고 할 때 각 문제의 알고리즘의 
  Worst case의 Time Complexity를 Asymptotic 하게 분석하여 제시하시오. (5점)
- 문제에서 구현하라고 지시한 부분 외의 코드는 "절대" 수정하지 마시오.
- 작성한 알고리즘이 정확하게 동작하더라도 
  최적의 알고리즘보다 Time Complexity가 나쁘면 10점 감점합니다.
"""
class List:
    class Node:
        def __init__(self, value, next_node):
            # Singly Linked List임.
            # 이 코드는 수정하지 마시오.
            self.value = value
            self.next = next_node

    def __init__(self):
        # Linked List는 헤드만 기억한다.
        # 이 코드는 수정하지 마시오.
        self.head = None

    def print(self, title):
        # 리스트를 프린트
        # 이 코드는 수정하지 마시오.
        p = self.head
        print(title, end=": ")
        while p:
            print(p.value, end="->")
            p = p.next
        print()

    def add(self, value):
        # 리스트의 head에 value를 추가
        # 이 코드는 수정하지 마시오.
        node = self.Node(value, self.head)
        self.head = node

    def empty(self):
        # 리스트의 내용을 비우고 빈 리스트로 만드는 코드를 작성하시오.
        # (1) 이 함수의 Worst case Time complexity는? n(1)
        # (2) 여기에 코드를 작성하시오.
        self.head = None
        return
        
    def add_in_order(self, value):
        # 현재의 리스트가 오름차순으로 정렬되어 있다고 가정하고
        # 리스트 상에서 오름차순을 유지할 수 있게 value를 추가하는 코드를 작성하시오.
        # 예: 1->5->7 에서 6을 추가하면 1->5->6->7
        # (1) 이 함수의 Worst case Time complexity는? O(N)
        # (2) 여기에 코드를 작성하시오.
        if self.head == None:
            self.add(value)
        else:
            current = self.head
            tmp = None
            while current:
                if value > current.value:
                    tmp = current
                    current = current.next
                    if current == None:
                        new_node = self.Node(value, current)
                        tmp.next = new_node
                else:
                    if tmp:
                        new_node = self.Node(value, current)
                        tmp.next = new_node
                    else:
                        self.add(value)
                    break
        return

    def concat(self, list):
        # 현재의 리스트 가장 뒤에 list를 연결하는 함수를 작성하시오.
        # list의 내용을 복사할 필요없이 링크만 연결하여
        # 현재 리스트에 인자로 주어진 list를 결합하는 형태로 작성하시오.
        # 예: 1->2 와 3->4를 concat하면 1->2->3->4
        # (위 add_in_order와는 별개의 문제이므로 정렬은 필요없음)
        # (1) 이 함수의 Worst case Time complexity는? O(N)
        # (2) 여기에 코드를 작성하시오.
        if self.head:
            current = self.head
            tmp = None
            while current:
                tmp = current
                current = current.next
            tmp.next = list.head
            return
        else:
            self.head = list.head
            return

    def reverse(self):
        # 현재 주어진 리스트의 순서를 뒤집은 리스트로 변환하는 함수를 작성하시오.
        # 예: A->B->C ==> C->B->A
        # 단, 새로운 노드를 하나도 만들지 않고 기존 노드만으로 뒤집으면 20점
        # 새로운 리스트나 노드를 만들서 해결하면 10점
        # (1) 이 함수의 Worst case Time complexity는? O(N)
        # (2) 여기에 코드를 작성하시오.
        current = self.head
        tmp = None
        while current:
            self.head = current.next
            current.next = tmp
            tmp = current
            current = self.head
        if self.head == None:
            self.head = tmp
        return




 # A B C D E
 # E D C B A
#====================
# 아래 테스트 코드는 수정하지 마시오!!!!
#====================
if __name__ == "__main__":
    # empty()를 구현 테스트

    # 실행결과
    # ---- Test empty() ----
    # LIST1: C->B->A->
    # LIST1:
    # LIST1: 1->2->3->
    print("---- Test empty() ----")
    list1 = List()
    list1.add('A')
    list1.add('B')
    list1.add('C')
    list1.print("LIST1")
    list1.empty()
    list1.print("LIST1")
    list1.add('3')
    list1.add('2')
    list1.add('1')
    list1.print("LIST1")

    # add_in_order()를 구현 테스트
    # 실행결과
    # ---- Test add_in_order ----
    # LIST2: B->C->D->E->
    # LIST2: A->B->C->D->E->
    # LIST2: A->B->C->D->E->F->
    print("---- Test add_in_order ----")
    list2 = List()
    list2.add_in_order('D')
    list2.add_in_order('B')
    list2.add_in_order('C')
    list2.add_in_order('E')
    list2.print("LIST2")
    list2.add_in_order('A')
    list2.print("LIST2")
    list2.add_in_order('F')
    list2.print("LIST2")

    # concat()를 구현 테스트
    # === 실행결과
    # ---- Test concat ----
    # LIST3: 1->2->
    # LIST4: 3->4->
    # LIST3: 1->2->3->4->
    # LIST4: 3->4->
    # LIST3:
    # LIST4: 3->4->
    # LIST3: 3->4->
    # LIST4: 3->4->
    print("---- Test concat ----")
    list3 = List()
    list3.add("2")
    list3.add("1")
    list3.print("LIST3")
    list4 = List()
    list4.add("4")
    list4.add("3")
    list4.print("LIST4")
    list3.concat(list4)
    list3.print("LIST3")
    list4.print("LIST4")

    list3 = List()
    list3.print("LIST3")
    list4.print("LIST4")

    list3.concat(list4)
    list3.print("LIST3")
    list4.print("LIST4")

    # reverse()를 구현 테스트
    # === 실행결과
    # ---- Test reverse ----
    # LIST5: A->B->C->
    # LIST5: C->B->A->
    # LIST6:
    # LIST6: 1->
    # LIST6: 1->
    print("---- Test reverse ----")
    list5 = List()
    list5.add("C")
    list5.add("B")
    list5.add("A")
    list5.print("LIST5")
    list5.reverse()
    list5.print("LIST5")
    list6 = List()
    list6.reverse()
    list6.print("LIST6")
    list6.add("1")
    list6.print("LIST6")
    list6.reverse()
    list6.print("LIST6")
