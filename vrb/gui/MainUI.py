# -*- coding: utf-8 -*-

import wx
import wx.xrc
from .MemberDialog import MemberDialog
from vrb.controller import ManagerController
from vrb.domain import MemberType


class MainUI(wx.Frame):

    def __init__(self):
        """Constructor"""
        super().__init__(parent=None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                         size=wx.Size(721, 506), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        sz_1 = wx.BoxSizer(wx.VERTICAL)
        sz_21 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)
        self.sz_1 = sz_1
        self.m_staticText37 = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"Member Count", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)
        sz_21.Add(self.m_staticText37, 0, wx.ALL | wx.EXPAND, 5)
        self.lbl_member_count = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.lbl_member_count.Wrap(-1)
        sz_21.Add(self.lbl_member_count, 0, wx.ALL, 5)
        sz_21.Add((32, 0), 0, wx.EXPAND, 5)
        self.m_staticText39 = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"Silver", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)
        sz_21.Add(self.m_staticText39, 0, wx.ALL, 5)
        self.lbl_sm_count = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_sm_count.Wrap(-1)
        sz_21.Add(self.lbl_sm_count, 0, wx.ALL, 5)
        self.m_staticText41 = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"Gold", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        sz_21.Add(self.m_staticText41, 0, wx.ALL, 5)
        self.lbl_gm_count = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_gm_count.Wrap(-1)
        sz_21.Add(self.lbl_gm_count, 0, wx.ALL, 5)

        self.m_staticText43 = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"Platinum", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        sz_21.Add(self.m_staticText43, 0, wx.ALL, 5)
        self.lbl_pm_count = wx.StaticText(sz_21.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_pm_count.Wrap(-1)
        sz_21.Add(self.lbl_pm_count, 0, wx.ALL, 5)
        sz_1.Add(sz_21, 0, wx.EXPAND, 5)
        sz_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)
        self.lbl_find = wx.StaticText(sz_2.GetStaticBox(), wx.ID_ANY, u"Find Member:", wx.DefaultPosition,
                                      wx.Size(100, -1), 0)
        self.lbl_find.Wrap(-1)
        sz_2.Add(self.lbl_find, 0, wx.ALL, 5)
        self.txt_find = wx.TextCtrl(sz_2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(200, -1), 0)
        sz_2.Add(self.txt_find, 0, wx.ALL, 5)
        sz_2.Add((32, 0), 0, wx.EXPAND, 5)
        self.btn_find = wx.Button(sz_2.GetStaticBox(), wx.ID_ANY, u"Find", wx.DefaultPosition, wx.DefaultSize, 0)
        sz_2.Add(self.btn_find, 0, wx.ALL, 5)
        sz_2.Add((32, 0), 1, wx.EXPAND, 5)
        self.btn_new_member = wx.Button(sz_2.GetStaticBox(), wx.ID_ANY, u"Add Member", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        sz_2.Add(self.btn_new_member, 0, wx.ALL, 5)
        sz_1.Add(sz_2, 0, wx.EXPAND, 5)
        sz_7 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Members"), wx.VERTICAL)
        self.lst_members = wx.ListCtrl(sz_7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        sz_7.Add(self.lst_members, 1, wx.ALL | wx.EXPAND, 5)
        sz_1.Add(sz_7, 1, wx.EXPAND, 5)
        self.SetSizer(sz_1)
        self.Layout()
        self.Centre(wx.BOTH)
        self.lst_members.InsertColumn(0, "Membership ID", width=150)
        self.lst_members.InsertColumn(1, "First Name", width=150)
        self.lst_members.InsertColumn(2, "Last Name", width=150)
        self.lst_members.InsertColumn(3, "Membership Level", width=150)
        self.list_dict = {}

        # Events
        self.btn_find.Bind(wx.EVT_BUTTON, self.find_member)
        self.btn_new_member.Bind(wx.EVT_BUTTON, self.add_member)
        self.lst_members.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.open_member)

        # Domain
        self._manager = ManagerController()
        self._manager.load_members()
        self.update_values()

    def __del__(self):
        pass

    def find_member(self, event):
        pass

    def add_member(self, event):
        dialog = MemberDialog(self, self._manager)
        print("[MainUI]: New member")
        dialog_result = dialog.ShowModal()
        dialog.Destroy()
        self.update_values()

    def open_member(self, event: wx.ListEvent):
        member_id: str = event.GetItem().GetText()
        print("[MainUI]: Open member: {}".format(member_id))
        dialog = MemberDialog(self, self._manager, member_id)
        dialog_result = dialog.ShowModal()
        if dialog_result == wx.ID_DELETE:
            self.lst_members.DeleteItem(self.list_dict.pop(member_id, None))
        dialog.Destroy()
        self.update_values()

    def update_values(self):
        self.lbl_member_count.SetLabel(str(self._manager.get_member_count()))
        self.lbl_sm_count.SetLabel(str(self._manager.get_member_count_for_type(MemberType.SILVER_MEMBER)))
        self.lbl_gm_count.SetLabel(str(self._manager.get_member_count_for_type(MemberType.GOLD_MEMBER)))
        self.lbl_pm_count.SetLabel(str(self._manager.get_member_count_for_type(MemberType.PLATINUM_MEMBER)))
        self.sz_1.Layout()

        for entry in self._manager.get_member_grid():
            member_id = entry[0]
            if member_id not in self.list_dict.keys():
                index = self.lst_members.InsertItem(self.lst_members.GetItemCount(), member_id)
                self.list_dict[member_id] = index
            else:
                index = self.list_dict[member_id]

            for column, text in enumerate(entry[1:]):
                self.lst_members.SetItem(index, column + 1, text)
