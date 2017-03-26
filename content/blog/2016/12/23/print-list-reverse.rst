##########################################
Print singly linked list in reverse order
##########################################

:date: 2016-12-23 00:05
:category: Data Struct & Algo
:tags: singly-linked-list, recursion
:summary: See above

Today, during the lunch break, I take a look at the following problem:

  Print a singly linked list in reverse order.

This is actually one of the interview questions I got at SAP for ABAP developer position
(luckily, they didn't offer me the position). I didn't get the correct answer at that time
and I think the problem may help me to kill some time during the break.

The question itself is not hard if you're familar with linked list and recursion philosophy:

.. code-block:: c

    static void
    printListReverseHelper(List L)
    {
      if (L == NULL)
      {
        return;
      }
      printListReverseHelper(L->Next);
      printf("%d->", L->Element);
    }

    void printListReverse(List L)
    {
      Pos dummyL = L->Next;
      printListReverseHelper(dummyL);
    }

Again, in our implementation of linked list, we use header node. Given the simiplicity of the problem,
I think it is good time to revisit some basic rules in recursion.

To be honest, recursion always gives me hard time because I always try to mentally expand all the call
stack and then work backwards to see if the recursion function gives what I expect. This is super energy
consuming and error-prone.

However, things start to get better since I start to read MAW. Here are the four basic rules of recursion
he emphasizes:

  1. *Base cases.* You must always have some base cases, which can be solved without recursion.
  2. *Making progress.* For the cases that are to be solved recursively, the recursive call must always
     be to a case that makes progress toward a base case.
  3. *Design rule.* Assume that all the recursive calls work.
  4. *Compound interest rule.* Never duplicate work by solving the same instance of a problem in separate
     recursive calls.

Among the four rules, No.3 rule is easily my most faviroite one. It is stated very simple but it has huge
impact on how you think about recursion.

Let's use first three rules to analyze this problem a little bit.

1. *Base cases.* This problem is quite simple. The base case is the case when the list is empty. In this case,
   we have nothing to do and simply return.
2. *Making progress.* This is reflected when we call ``printListReverseHelper(L->Next)``. Each time we make the
   recursive call, we pass in ``L->Next``, which makes the list shorter. This eventually will make the whole list
   empty, which is the base case.
3. *Design rule.* I use this rule to design the whole recursion function. Just imagaine a scenario like the following:
   Suppose you have a list of ``1->2->3``. Then, by the rule, we assume that the number ``2`` and ``3`` are already printed
   in reverse order. What we left to do is to print out ``1`` and then we done. We follow this thought process closely
   when we actually write the recursion function. After we write out the base case, we first write ``printListReverseHelper(L->Next);``
   This is saying that the rest of list (except the first one) is already printed in reverse order (i.e. ``2`` and ``3`` in our case).
   Then we write ``printf("%d->", L->Element);``. This says, ok, since we are only left with the first node, let's print it out and the
   job is done (i.e. ``1`` in our case).

See, how simple the recursion can be if we can actually get over psychological obstacle to expand the call stack mentally and directly apply
four rules (especially the third rule) to design our function.
