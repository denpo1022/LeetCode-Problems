class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder: return []
        folder.sort(key=len)
        folder = [i + '/' for i in folder]
        for element in folder:
            backard_target = len(folder) - 1
            while(len(element) < len(folder[backard_target])):
                if(str(element) in str(folder[backard_target])):
                    del folder[backard_target]
                backard_target -= 1
        folder = [i[:-1] for i in folder]
        return folder