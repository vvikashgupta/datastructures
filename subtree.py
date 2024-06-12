i        def preorder(t , leftflag):
            if t == None:
                if leftflag:
                    return 'lnull'
                else:
                    return 'rnull'
            return "#" + str(t.val) + " " + preorder(t.left , True) + " " + preorder(t.right, False)
        st1 = preorder(s,True)
        st2 = preorder(t,True)
        if st2 in st1:
            return True
        else:
            return False
        
        def isequal(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val == t.val and isequal(s.left , t.left) and isequal(s.right,t.right):
                return True
            else:
                return False
        if s != None and isequal(s,t) or isSubtree(s.left , t) or isSubtree(s.right,t):
            return True
        else:
            return False

