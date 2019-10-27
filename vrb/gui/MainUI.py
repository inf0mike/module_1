import wx
import wx.xrc
from .MemberDialog import MemberDialog
from vrb.controller import ManagerController
from vrb.domain import MemberType


# MainUI class is the parent UI element for this part of the application
# Note: all of the GUI initialisation code is generated using a designer tool (wxFormBuilder)
class MainUI(wx.Frame):

    # Constructor
    def __init__(self):
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
        # sz_2.Add((32, 0), 0, wx.EXPAND, 5)
        self.btn_find_clear = wx.Button(sz_2.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        sz_2.Add(self.btn_find_clear, 0, wx.ALL, 5)
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
        self.btn_find_clear.Bind(wx.EVT_BUTTON, self._find_clear)
        self.btn_new_member.Bind(wx.EVT_BUTTON, self._add_member)
        self.lst_members.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self._open_member)
        self.txt_find.Bind(wx.EVT_TEXT, self._on_find_text)

        # Domain
        self._manager = ManagerController("/Users/mike/file.json")
        self._manager.load_members()
        self._update_values()

    # Python destructor
    def __del__(self):
        pass

    # Event handler for text changes in the search text box
    def _on_find_text(self, event):
        # just update ui
        self._update_values()

    # Event handler for the clear button on the find box
    def _find_clear(self, event):
        # just reset it to an empty string
        self.txt_find.SetValue("")

    # Event handler for the Add Member button  This opens the MemberDialog UI
    def _add_member(self, event):
        # Instantiate the dialog and keep a reference. Pass a reference to the ManagerController
        # but no member details because this is a new member
        dialog = MemberDialog(self, self._manager)
        print("[MainUI]: New member")
        # Show the dialog UI as a modal to prevent users changing things in this UI screen
        dialog.ShowModal()
        # After dialog is closed, destroy it
        dialog.Destroy()
        # refresh the screen data
        self._update_values()

    # Event handler for selecting a member from the UI list. This also opens the MemberDialog UI
    def _open_member(self, event: wx.ListEvent):
        # Get the member_id that is provided in the event data from the line item that was double clicked
        member_id: str = event.GetItem().GetText()
        print("[MainUI]: Open member: {}".format(member_id))
        # Instantiate the dialog and keep a reference. Pass a reference to the ManagerController
        # AND the member_id so the MemberDialog can show the details for the selected Member
        dialog = MemberDialog(self, self._manager, member_id)
        # Show the MemberUI as a modal dialog and capture the result
        dialog_result = dialog.ShowModal()
        # This is just for information
        if dialog_result == wx.ID_DELETE:
            print("Performed a DELETE operation")
        # After dialog is closed, destroy it
        dialog.Destroy()
        # refresh the screen data
        self._update_values()

    # Screen items data population and refresh
    def _update_values(self):
        # ask the controller for member counts and update the values in the UI elements
        self.lbl_member_count.SetLabel(str(self._manager.get_member_count()))
        self.lbl_sm_count.SetLabel(str(self._manager.get_member_count_for_type(MemberType.SILVER_MEMBER)))
        self.lbl_gm_count.SetLabel(str(self._manager.get_member_count_for_type(MemberType.GOLD_MEMBER)))
        self.lbl_pm_count.SetLabel(str(self._manager.get_member_count_for_type(MemberType.PLATINUM_MEMBER)))
        # ask wxWidgets to apply the static text changes
        self.sz_1.Layout()

        # empty the member list control
        self.lst_members.DeleteAllItems()
        # also empty the tracking dictionary
        self.list_dict.clear()

        # request a list of filtered member tuples from the controller and
        # iterate through the member data to populate the list control
        for entry in self._manager.get_filtered_member_display_data(self.txt_find.GetValue()):
            # member_id is always the first entry
            member_id = entry[0]
            # check our tracking dict for the member_id
            if member_id not in self.list_dict.keys():
                # didn't know about this member so create a new list item entry
                index = self.lst_members.InsertItem(self.lst_members.GetItemCount(), member_id)
                # And store the index in our tracking dict
                self.list_dict[member_id] = index
            else:
                # otherwise, get the list index number from our tracking dict
                index = self.list_dict[member_id]

            # Now populate the rest of the columns for this member
            for column, text in enumerate(entry[1:]):
                self.lst_members.SetItem(index, column + 1, text)
