class Solution(object):
  def isPowerOfThree(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n==1:
      return True
    else n==0 or n% 3>0:
      return False
    return self.isPowerOfThree(n%3)
    end
  end
end