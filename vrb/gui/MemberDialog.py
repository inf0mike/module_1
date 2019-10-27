from typing import Optional

import wx
import wx.xrc
import wx.adv
from vrb.controller import ManagerController, BookingController
from vrb.domain import Member, MemberType, Address
from datetime import datetime
from enum import Enum

MEMBER_TYPES = {
    "SilverMember": 0,
    "GoldMember": 1,
    "PlatinumMember": 2
}


# MemberDialog class defines UI for editing members
# Note: all of the GUI initialisation code is generated using a designer tool (wxFormBuilder)
class MemberDialog(wx.Dialog):
    _manager: ManagerController
    _bookings: BookingController

    def __init__(self, parent, manager=None, member_id=None):
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

        sz_info_labels = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText275 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Joined", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText275.Wrap(-1)

        sz_info_labels.Add(self.m_staticText275, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText2751 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition,
                                              wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText2751.Wrap(-1)

        sz_info_labels.Add(self.m_staticText2751, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText2721 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Fee Paid", wx.DefaultPosition,
                                              wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText2721.Wrap(-1)

        sz_info_labels.Add(self.m_staticText2721, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText2731 = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"Prior Bookings", wx.DefaultPosition,
                                              wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText2731.Wrap(-1)
        sz_info_labels.Add(self.m_staticText2731, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        bSizer13.Add(sz_info_labels, 0, 0, 5)
        bSizer13.Add((0, 0), 0, wx.EXPAND, 5)
        sz_info = wx.BoxSizer(wx.VERTICAL)
        self._sz_info = sz_info
        sz_info.SetMinSize(wx.Size(200, -1))
        self.st_joined = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.st_joined.Wrap(-1)

        sz_info.Add(self.st_joined, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.st_status = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_status.Wrap(-1)

        sz_info.Add(self.st_status, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.st_fee = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_fee.Wrap(-1)

        sz_info.Add(self.st_fee, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.st_bookings = wx.StaticText(sz_3.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_bookings.Wrap(-1)

        sz_info.Add(self.st_bookings, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        bSizer13.Add(sz_info, 0, wx.EXPAND, 5)

        sz_3.Add(bSizer13, 0, wx.EXPAND | wx.TOP, 5)
        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer18.Add((0, 0), 1, wx.EXPAND, 5)
        self.btn_member_delete = wx.Button(sz_3.GetStaticBox(), wx.ID_ANY, u"Delete Member", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.btn_member_delete.SetForegroundColour(wx.Colour(251, 0, 7))
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
        self._member_id = member_id

        # Connect Events
        self.txt_first_name.Bind(wx.EVT_TEXT, self._check_name_fields)
        self.txt_last_name.Bind(wx.EVT_TEXT, self._check_name_fields)
        self.btn_member_delete.Bind(wx.EVT_BUTTON, self._member_delete)
        self.btn_member_save.Bind(wx.EVT_BUTTON, self._member_save)
        self.btn_member_cancel.Bind(wx.EVT_BUTTON, self.ev_member_cancel)

        # Disable the save button to start with
        self.btn_member_save.Enable(False)

        # Disable the delete button if this is a new member form
        if member_id is None:
            self.btn_member_delete.Enable(False)

        # Hide the member_id field for new members as we dont have one yet
        if member_id is None:
            self.txt_member_id.Show(False)

        # Here we generate a BookingController.  For early prototype this is a stub service
        self._bookings = BookingController()

        # keep a reference to the manager controller
        self._manager = manager
        # update the UI now that its ready
        self._populate_form()

    def __del__(self):
        print("[MemberDialog]: Destroyed")

    # Event handler for on text change events in the first name or last name fields
    # enables the save button when both are not empty
    def _check_name_fields(self, event: wx.Event):
        if self.txt_first_name.GetValue() != "" and self.txt_last_name.GetValue() != "":
            self.btn_member_save.Enable(True)
        else:
            self.btn_member_save.Enable(False)

    # Load up the UI form with the member data or do nothing if there is no member specified (new member)
    def _populate_form(self) -> None:
        # Skip for new member, nothing to do
        if self._member_id is None:
            return

        # Existing members must have first / last name so enable save button
        self.btn_member_save.Enable(False)
        # get the member object
        member: Optional[Member] = self._manager.get_member(self._member_id)
        # update the form fields
        self.txt_member_id.SetValue(member.id)
        self.txt_first_name.SetValue(member.first_name)
        self.txt_last_name.SetValue(member.last_name)
        # convert the text iso format date from the underlying data into a wx.DateTime object
        # and set the date of birth control to use it
        self.dp_date_of_birth.SetValue(wx.DateTime(datetime.fromisoformat(member.date_of_birth)))
        # get the members addresses list
        addresses = member.get_address_list()
        if len(addresses) > 0:
            # we are only going to allow editing for one address so get the first one in the list
            address = addresses[0]
            # update the form fields
            self.txt_address_1.SetValue(address.line1)
            self.txt_address_2.SetValue(address.line2)
            self.txt_address_3.SetValue(address.line3)
            self.txt_address_4.SetValue(address.line4)
            self.txt_post_code.SetValue(address.post_code)
        # update the member level choice field to reflect what the current membership level is
        self.ddl_member_type.Select(MEMBER_TYPES[member.__class__.__name__])
        # populate fee paid for this member
        self.st_fee.SetLabel(self._bookings.get_fees_paid_for(self._member_id))
        self.st_bookings.SetLabel(str(len(self._bookings.get_bookings_for(self._member_id))))
        self.st_status.SetLabel(self._get_member_status(member))
        self.st_joined.SetLabel(member.joined_date)
        self._sz_info.Layout()

    # determine status
    def _get_member_status(self, member: Member) -> str:
        result = "Valid Membership"
        if member.__class__.__name__ == "GoldMember" and len(
                self._bookings.get_bookings_for(self._member_id)) < member.booking_threshold:
            result = "INVALID: Not enough bookings"
        if member.__class__.__name__ == "PlatinumMember" and int(self._bookings.get_fees_paid_for(
                self._member_id)) < member.membership_fee:
            result = "INVALID: Fees not paid"
        return result

    # Event handler for the delete member button
    def _member_delete(self, event: wx.Event) -> None:
        # Show a modal are you sure box
        result = wx.MessageBox("Are you sure you want to delete this member?", "Confirm", wx.YES_NO)
        # if they agreed...
        if result == wx.YES:
            # instruct the controller to remove this user
            self._manager.delete_member(self._member_id)
            # set the return code on our own UI
            self.EndModal(wx.ID_DELETE)
        # and close ourselves
        self.Close()

    # Event handler for save button
    def _member_save(self, event: wx.Event) -> None:
        # update data from form data
        self._update_member_from_form()
        # instruct controller to save the members
        self._manager.save_members()
        # set a return value
        self.EndModal(2)
        # and close ourselves
        self.Close()

    # Event handler for cancel button
    def ev_member_cancel(self, event: wx.Event) -> None:
        # set a return value
        self.EndModal(0)
        # and close ourselves
        self.Close()

    # read data from UI form and populate the data model with it
    def _update_member_from_form(self):
        # determine what the member level (type) should be from choice field
        member_level: Enum = MemberType.get_type_from_value(self.ddl_member_type.GetSelection())
        # get each of the form field values
        dob: wx.DateTime = self.dp_date_of_birth.GetValue()
        first_name = self.txt_first_name.GetValue()
        last_name = self.txt_last_name.GetValue()
        post_code = self.txt_post_code.GetValue()
        line1 = self.txt_address_1.GetValue()
        line2 = self.txt_address_2.GetValue()
        line3 = self.txt_address_3.GetValue()
        line4 = self.txt_address_4.GetValue()

        # for existing members:
        if self._member_id is not None:
            # get the member object
            member: Optional[Member] = self._manager.get_member(self._member_id)
            # if the membership level is different to before
            if member.__class__.__name__ != member_level.value:
                # then get a new membership class at the new level
                member = self._manager.update_membership_level(self._member_id, member_level)
            # convert the wx.DateTime to and iso string and assign it to the member object
            member.date_of_birth = dob.FormatISODate()
            # continue to update data in the member object
            member.first_name = first_name
            member.last_name = last_name
            address: Address = member.get_address_list()[0]
            address.line1 = line1
            address.line2 = line2
            address.line3 = line3
            address.line4 = line4
            address.post_code = post_code
            print("[MemberDialog]: Updated: {}".format(member.id))
        else:
            # new members can be simply created by the controller
            member: Optional[Member] = self._manager.add_member(
                first_name, last_name, dob.FormatISODate(),
                line1, line2, line3, line4,
                post_code, member_level.value
            )
            print("[MemberDialog]: Created: {}".format(member.id))
