class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 看到这种来来回回，增增删删的题，一般都想到用栈。
        # 这道题要理解简化path的规则
        
        # 遇到"."就跳过，遇到".."就删减一个元素
        
        stack = list()
        print("ss")
        print(stack)
        path = [p for p in path.split("/") if p]
        print(path)
        for p in path:
            if p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
                    print(stack)
            else:
                stack.append(p)
        print("finallll")
        print(stack)
        return "/" + "/".join(stack)