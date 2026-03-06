import qrcode
from config import Config
import io

def generate_upi_qr(amount):
    # UPI Deep Link Structure
    # pa: UPI ID, pn: Name, am: Amount, cu: Currency, tn: Note
    upi_link = f"upi://pay?pa={Config.UPI_ID}&pn={Config.MERCHANT_NAME}&am={amount}&cu=INR&tn=Premium_Purchase"
    
    # QR Code generation
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(upi_link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to memory instead of local file for speed
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr
  
