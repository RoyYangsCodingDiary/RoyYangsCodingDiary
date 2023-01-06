Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Option Explicit

Sub CalculateBoughtCosts()

Dim Prices() As Variant
Dim SeatsAvailable() As Variant
Dim SeatsRequired() As Variant
Dim BookingFees() As Variant

Dim AllSeatsCosts(1 To 10, 1 To 7) As Double
Dim SeatsBought(1 To 10, 1 To 7) As Integer
Dim BoughtSeatsCost(1 To 10, 1 To 7) As Double

Dim Num_Weeks As Integer
Num_Weeks = 10
Dim iWeek As Integer
Dim iDay As Integer

Dim TotalCost As Double
Dim TotalSeats As Double

Prices = ws_flightpurchases.Range("Prices").Resize(Num_Weeks, 7).Value
SeatsAvailable() = ws_flightpurchases.Range("SeatsAvailable").Resize(Num_Weeks, 7).Value
SeatsRequired() = ws_flightpurchases.Range("SeatsRequired").Resize(Num_Weeks, 7).Value
BookingFees() = ws_flightpurchases.Range("BookingFees").Resize(1, 7).Value

Dim SeatsRequired As Integer
Dim SeatsAvailable As Integer
Dim SeatPrice As Double
Dim SeatFee As Double
Dim SeatTotalPrice As Double

For iWeek = 1 To Num_Weeks
    For iDay = 1 To 7
    AllSeatsCosts(iWeek, iDay) = Prices(iWeek, iDay) * SeatsAvailable(iWeek, iDay)
        
        SeatsRequired = SeatsRequired(iWeek, iDay)
        SeatsAvailable = SeatsAvailable(iWeek, iDay)
        SeatPrice = Prices(iWeek, iDay)
        SeatFee = BookingFees(1, iDay)
        SeatTotalPrice = SeatPrice + SeatFee
        
        If SeatsRequired > SeatsAvailable Then
                SeatsBought(iWeek, iDay) = SeatsAvailable
                BoughtSeatsCost(iWeek, iDay) = SeatsAvailable * SeatTotalPrice
                TotalCost = TotalCost + (SeatsAvailable * SeatTotalPrice)
                TotalSeats = TotalSeats + SeatsAvailable
            Else
                SeatsBought(iWeek, iDay) = SeatsRequired
                BoughtSeatsCost(iWeek, iDay) = SeatsRequired * SeatTotalPrice
                TotalCost = TotalCost + (SeatsRequired * SeatTotalPrice)
                TotalSeats = TotalSeats + SeatsRequired
        End If
        
    Next iDay
Next iWeek

ws_flightpurchases.Range("AllSeatsCost").Resize(Num_Weeks, 7).Value = AllSeatsCosts()
ws_flightpurchases.Range("SeatsBought").Resize(Num_Weeks, 7).Value = SeatsBought()
ws_flightpurchases.Range("BoughtSeatsCost").Resize(Num_Weeks, 7).Value = BoughtSeatsCost()
ws_flightpurchases.Range("TotalCost") = TotalCost
ws_flightpurchases.Range("TotalSeats") = TotalSeats

End Sub


Sub CalculateBoughtCostsAlternativeSyntax()

Dim Prices() As Variant
Dim SeatsAvailable() As Variant
Dim SeatsRequired() As Variant
Dim BookingFees() As Variant

Dim AllSeatsCosts(1 To 10, 1 To 7) As Double
Dim SeatsBought(1 To 10, 1 To 7) As Integer
Dim BoughtSeatsCost(1 To 10, 1 To 7) As Double

Dim Num_Weeks As Integer
Num_Weeks = 10
Dim iWeek As Integer
Dim iDay As Integer

Dim TotalCost As Double
Dim TotalSeats As Double

Prices = ws_flightpurchases.Range("Prices").Resize(Num_Weeks, 7).Value
SeatsAvailable() = ws_flightpurchases.Range("SeatsAvailable").Resize(Num_Weeks, 7).Value
SeatsRequired() = ws_flightpurchases.Range("SeatsRequired").Resize(Num_Weeks, 7).Value
BookingFees() = ws_flightpurchases.Range("BookingFees").Resize(1, 7).Value

For iWeek = 1 To Num_Weeks
    For iDay = 1 To 7
        AllSeatsCosts(iWeek, iDay) = Prices(iWeek, iDay) * SeatsAvailable(iWeek, iDay)
        If SeatsRequired(iWeek, iDay) > SeatsAvailable(iWeek, iDay) Then
                SeatsBought(iWeek, iDay) = SeatsAvailable(iWeek, iDay)
                BoughtSeatsCost(iWeek, iDay) = SeatsBought(iWeek, iDay) * (Prices(iWeek, iDay) + BookingFees(1, iDay))
                TotalCost = TotalCost + BoughtSeatsCost(iWeek, iDay)
                TotalSeats = TotalSeats + SeatsBought(iWeek, iDay)
            Else
                SeatsBought(iWeek, iDay) = SeatsRequired(iWeek, iDay)
                BoughtSeatsCost(iWeek, iDay) = SeatsBought(iWeek, iDay) * (Prices(iWeek, iDay) + BookingFees(1, iDay))
                TotalCost = TotalCost + BoughtSeatsCost(iWeek, iDay)
                TotalSeats = TotalSeats + SeatsBought(iWeek, iDay)
        End If
        
    Next iDay
Next iWeek

ws_flightpurchases.Range("AllSeatsCost").Resize(Num_Weeks, 7).Value = AllSeatsCosts()
ws_flightpurchases.Range("SeatsBought").Resize(Num_Weeks, 7).Value = SeatsBought()
ws_flightpurchases.Range("BoughtSeatsCost").Resize(Num_Weeks, 7).Value = BoughtSeatsCost()
ws_flightpurchases.Range("TotalCost") = TotalCost
ws_flightpurchases.Range("TotalSeats") = TotalSeats

End Sub
