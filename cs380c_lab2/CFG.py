import collections
class BasicBlock(object):
    def __init__(self, st_instr_id, ed_instr_id, func_instr_id):
        super(BasicBlock, self).__init__()
        self.name = st_instr_id
        self.st_instr_id = st_instr_id
        self.ed_instr_id = ed_instr_id
        self.func_instr_id = func_instr_id

class CFG(object):
    '''
    Abbreviations:
    - bb: basic block
    - bbn: basic block name
    '''
    def __init__(self):
        super(CFG, self).__init__()
        self.bbns_of_func = collections.defaultdict(set)
        self.bbs = dict()
        self.edges = collections.defaultdict(list)

    def add_basic_block(self, bb):
        self.bbs[bb.name] = bb
        self.bbns_of_func[bb.func_instr_id].add(bb.name)
        return self

    def add_edge(self, src_bb, dst_bb):
        '''
        src_bb and dst_bb can be strings, which enables adding edges before relevant bbs are created!
        '''
        src_bbn = src_bb if not isinstance(src_bb, BasicBlock) else src_bb.name
        dst_bbn =  dst_bb if not isinstance(dst_bb, BasicBlock) else dst_bb.name
        # if self.bbs[src_bbn].func_instr_id != self.bbs[dst_bbn].func_instr_id:
        #     return self
        self.edges[src_bbn].append(dst_bbn)
        return self

    def _sort(self):
        for func in self.bbns_of_func.keys():
            self.bbns_of_func[func] = sorted(self.bbns_of_func[func])
        for src_bbn in self.edges.keys():
            self.edges[src_bbn]  = sorted(self.edges[src_bbn])
        return self

    def display(self):
        self._sort()
        for func in sorted(self.bbns_of_func.keys()):
            bbns = self.bbns_of_func[func]
            print 'Function: %s\nBasic blocks: %s\nCFG:\n' % (func, ' '.join(map(str, bbns)))
            for src_bbn in bbns:
                dst_bbns = self.edges[src_bbn]
                print '%s ->%s\n' % (src_bbn, '' if len(dst_bbns) == 0 else (' ' + ' '.join(map(str, dst_bbns))))
        return self