class Solution(object):
	def sumOfLeftLeaves(self, root):
		sum = 0
		stack = [root]
		visited = []
		while stack:
			current = stack.pop()
			if current not in visited:
				visited.append(current)
				if current.left != None:
					stack.append(current.left)
					if current.left.left == None and current.left.right == None:
						sum += current.left.val
				if current.right != None:
					stack.append(current.right)
		return sum

		
		