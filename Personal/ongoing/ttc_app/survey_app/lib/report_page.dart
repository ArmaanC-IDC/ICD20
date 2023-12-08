import 'package:flutter/material.dart';
import 'view_page.dart';

class ReportPage extends StatelessWidget {
  final TextEditingController locationController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Report Page'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('What is the location of the stuff?'),
            SizedBox(height: 20),
            TextField(
              controller: locationController,
              decoration: InputDecoration(labelText: 'Location'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                submitResponse(context);
              },
              child: Text('Submit'),
            ),
          ],
        ),
      ),
    );
  }

  void submitResponse(BuildContext context) {
    String location = locationController.text.trim();
    if (location.isNotEmpty) {
      // Check if the location is not empty
      // Add the response to the list
      ViewPage.responses.add('Location: $location');
      Navigator.pop(context);
    } else {
      // Handle case where location is empty
      // You can show an error message or take other actions
    }
  }
}
