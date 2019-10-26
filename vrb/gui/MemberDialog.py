import wx
import wx.xrc
import wx.adv
from vrb.controller import ManagerController


class MemberDialog(wx.Dialog):
    _manager: ManagerController

    def __init__(self, parent, manager=None, member=None):
        super().__init__(parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                         size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        sz_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        sz_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl_first_name = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                            wx.Size(100, -1), 0)
        self.lbl_first_name.Wrap(-1)
        sz_4.Add(self.lbl_first_name, 0, wx.RIGHT | wx.LEFT, 5)
        self.txt_first_name = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(200, -1), 0)
        sz_4.Add(self.txt_first_name, 0, wx.RIGHT | wx.LEFT, 5)
        sz_4.Add((32, 0), 0, wx.EXPAND, 5)
        self.lbl_member_id = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Membership ID", wx.DefaultPosition,
                                           wx.Size(100, -1), 0)
        self.lbl_member_id.Wrap(-1)
        sz_4.Add(self.lbl_member_id, 0, wx.RIGHT | wx.LEFT, 5)
        self.txt_member_id = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(200, -1), wx.TE_READONLY)
        sz_4.Add(self.txt_member_id, 0, wx.RIGHT | wx.LEFT, 5)
        if member is None:
            self.txt_member_id.Show(False)
        sz_3.Add(sz_4, 1, wx.EXPAND | wx.TOP, 5)
        sz_5 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl_last_name = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                           wx.Size(100, -1), 0)
        self.lbl_last_name.Wrap(-1)
        sz_5.Add(self.lbl_last_name, 0, wx.ALIGN_CENTER | wx.RIGHT | wx.LEFT, 5)
        self.txt_last_name = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(200, -1), 0)
        sz_5.Add(self.txt_last_name, 0, wx.ALIGN_CENTER | wx.RIGHT | wx.LEFT, 5)
        sz_5.Add((32, 0), 0, wx.EXPAND, 5)
        self.lbl_dob = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                     wx.Size(100, -1), 0)
        self.lbl_dob.Wrap(-1)
        sz_5.Add(self.lbl_dob, 0, wx.ALIGN_CENTER | wx.RIGHT | wx.LEFT, 5)
        self.dp_date_of_birth = wx.adv.DatePickerCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.Size(100, -1), wx.adv.DP_DEFAULT)
        sz_5.Add(self.dp_date_of_birth, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)
        sz_3.Add(sz_5, 1, wx.EXPAND, 5)
        sz_6 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl_mem_level = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Member Level", wx.DefaultPosition,
                                           wx.Size(100, -1), 0)
        self.lbl_mem_level.Wrap(-1)
        sz_6.Add(self.lbl_mem_level, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        ddl_member_typeChoices = [u"Silver Membership", u"Gold Membership", u"Platinum Membership"]
        self.ddl_member_type = wx.Choice(sz_3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(200, -1),
                                         ddl_member_typeChoices, 0)
        self.ddl_member_type.SetSelection(0)
        sz_6.Add(self.ddl_member_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sz_6.Add((32, 0), 0, wx.EXPAND, 5)
        sz_3.Add(sz_6, 1, wx.EXPAND, 5)
        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer13.Add((30, 0), 0, wx.EXPAND, 5)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText27 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Address", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText27.Wrap(-1)
        bSizer11.Add(self.m_staticText27, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)
        self.m_staticText271 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText271.Wrap(-1)
        bSizer11.Add(self.m_staticText271, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText272 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText272.Wrap(-1)
        bSizer11.Add(self.m_staticText272, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)
        self.m_staticText273 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText273.Wrap(-1)
        bSizer11.Add(self.m_staticText273, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)
        self.m_staticText274 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Post Code", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText274.Wrap(-1)
        bSizer11.Add(self.m_staticText274, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        bSizer13.Add(bSizer11, 0, 0, 5)
        bSizer111 = wx.BoxSizer(wx.VERTICAL)
        bSizer111.SetMinSize(wx.Size(200, -1))
        self.txt_address_1 = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(100, -1), 0)
        bSizer111.Add(self.txt_address_1, 1, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        self.txt_address_2 = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer111.Add(self.txt_address_2, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        self.txt_address_3 = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer111.Add(self.txt_address_3, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        self.txt_address_4 = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer111.Add(self.txt_address_4, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        self.txt_post_code = wx.TextCtrl(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer111.Add(self.txt_post_code, 1, wx.RIGHT | wx.LEFT, 5)
        bSizer13.Add(bSizer111, 0, 0, 5)
        sz_3.Add(bSizer13, 0, wx.EXPAND | wx.TOP, 5)
        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer18.Add((0, 0), 1, wx.EXPAND, 5)
        self.btn_member_delete = wx.Button(sz_3.GetStaticBox(), wx.ID_ANY, u"Delete Member", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.btn_member_delete.SetForegroundColour(wx.Colour(251, 0, 7))
        if member is None:
            self.btn_member_delete.Enable(False)
        bSizer18.Add(self.btn_member_delete, 0, wx.ALL, 5)
        bSizer18.Add((20, 0), 0, wx.EXPAND, 5)
        self.btn_member_save = wx.Button(sz_3.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.btn_member_save, 0, wx.ALL, 5)
        self.btn_member_cancel = wx.Button(sz_3.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer18.Add(self.btn_member_cancel, 0, wx.ALL, 5)
        sz_3.Add(bSizer18, 1, wx.EXPAND, 5)
        self.SetSizer(sz_3)
        self.Layout()
        sz_3.Fit(self)
        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_member_delete.Bind(wx.EVT_BUTTON, self.ev_member_delete)
        self.btn_member_save.Bind(wx.EVT_BUTTON, self.ev_member_save)
        self.btn_member_cancel.Bind(wx.EVT_BUTTON, self.ev_member_cancel)

        self._manager = manager
        print(self._manager.get_member_id_list())

    def __del__(self):
        print("[MemberDialog]: Destroyed")

    def ev_member_delete(self, event):
        result = wx.MessageBox("Are you sure you want to delete this member?", "Confirm", wx.YES_NO)
        if result == wx.YES:
            self.EndModal(10)
        else:
            self.EndModal(20)
        self.Close()

    def ev_member_save(self, event):
        self.EndModal(2)
        self.Close()

    def ev_member_cancel(self, event):
        self.EndModal(0)
        self.Close()
